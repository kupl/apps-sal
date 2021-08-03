class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        D = set()

        while True:
            changes = False
            last_str = ''
            for i, ch in enumerate(A[0]):
                if i not in D:
                    last_str += ch
            for x in A[1:]:
                this_str = ''
                this_idx = []
                for i, ch in enumerate(x):
                    if i not in D:
                        this_str += ch
                        this_idx.append(i)
                while this_str < last_str:
                    for i in range(len(this_str)):
                        if this_str[i] < last_str[i]:
                            D.add(this_idx[i])
                            this_idx = this_idx[:i] + this_idx[i + 1:]
                            this_str = this_str[:i] + this_str[i + 1:]
                            last_str = last_str[:i] + last_str[i + 1:]
                            changes = True
                            break
                last_str = this_str
            if not changes:
                break
        return len(D)
