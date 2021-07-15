EVEN = 0
ODD = 1

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        A_sorted = []
        for i, a in enumerate(A):
            item = (a, i)
            A_sorted.append(item)
        A_sorted.sort()
        
        odd_jmp_dct = {}
        # Create dct of reversed odd jumps
        for i, item in enumerate(A_sorted):
            a, idx = item
            if idx == len(A) - 1:
                continue
            # find where a can jump to
            j = i + 1
            if j >= len(A_sorted):
                continue
            next_a, next_idx = A_sorted[j]
            while j < len(A_sorted) - 1 and next_idx < idx:
                j += 1
                next_a, next_idx = A_sorted[j]
            if next_idx > idx:
                try:
                    odd_jmp_dct[next_idx].add(idx)
                except KeyError:
                    odd_jmp_dct[next_idx] = set([idx])
        
        A_sorted.sort(key=lambda x: (-x[0], x[1]))
        even_jmp_dct = {}
        # Create dct of reversed even jumps
        for i, item in enumerate(A_sorted):
            a, idx = item
            if idx == len(A) - 1:
                continue
            # find where a can jump to
            j = i + 1
            if j >= len(A_sorted):
                continue
            next_a, next_idx = A_sorted[j]
            while j < len(A_sorted) - 1 and next_idx < idx:
                j += 1
                next_a, next_idx = A_sorted[j]
            if next_idx > idx:
                try:
                    even_jmp_dct[next_idx].add(idx)
                except KeyError:
                    even_jmp_dct[next_idx] = set([idx])
        # print(odd_jmp_dct)
        # print(even_jmp_dct)
        # Try traversing through graph from end node to any other nodes
        q = collections.deque()
        item1 = (len(A) - 1, EVEN) # (<index>, <jump type>)
        item2 = (len(A) - 1, ODD)
        q.append(item1)
        q.append(item2)
        
        ans = set([len(A) - 1])
        
        while q:
            # print(q)
            i, jump_type = q.popleft()
            if jump_type == ODD:
                if i not in odd_jmp_dct:
                    continue
                for new_i in odd_jmp_dct[i]:
                    new_item = (new_i, EVEN)
                    ans.add(new_i)
                    q.append(new_item)
            else:
                if i not in even_jmp_dct:
                    continue
                for new_i in even_jmp_dct[i]:
                    new_item = (new_i, ODD)
                    q.append(new_item)
        return len(ans)

