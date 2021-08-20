class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        last_found = -1
        hash_size = {}
        hash_chunks = {}
        for i in range(len(arr)):
            num = arr[i] - 1
            if num == 0:
                if num + 1 not in hash_chunks:
                    hash_chunks[num] = (num, num, 1)
                    hash_size[1] = 1 + hash_size.get(1, 0)
                else:
                    (start, end, size) = hash_chunks[num + 1]
                    new_start = num
                    end = end
                    new_size = size + 1
                    hash_chunks[end] = (new_start, end, new_size)
                    hash_chunks[num] = (new_start, end, new_size)
                    hash_size[size] -= 1
                    hash_size[new_size] = 1 + hash_size.get(new_size, 0)
            elif num == len(arr) - 1:
                if num - 1 not in hash_chunks:
                    hash_chunks[num] = (num, num, 1)
                    hash_size[1] = 1 + hash_size.get(1, 0)
                else:
                    (start, end, size) = hash_chunks[num - 1]
                    start = start
                    new_end = num
                    new_size = size + 1
                    hash_chunks[start] = (start, new_end, new_size)
                    hash_chunks[num] = (start, new_end, new_size)
                    hash_size[size] -= 1
                    hash_size[new_size] = 1 + hash_size.get(new_size, 0)
            elif num + 1 in hash_chunks and num - 1 in hash_chunks:
                (f_start, f_end, f_size) = hash_chunks[num - 1]
                (b_start, b_end, b_size) = hash_chunks[num + 1]
                new_front = f_start
                new_end = b_end
                new_size = f_size + b_size + 1
                hash_chunks[f_start] = (new_front, new_end, new_size)
                hash_chunks[b_end] = (new_front, new_end, new_size)
                hash_size[f_size] -= 1
                hash_size[b_size] -= 1
                hash_size[new_size] = 1 + hash_size.get(new_size, 0)
            elif num + 1 in hash_chunks:
                (start, end, size) = hash_chunks[num + 1]
                new_start = num
                end = end
                new_size = size + 1
                hash_chunks[end] = (new_start, end, new_size)
                hash_chunks[num] = (new_start, end, new_size)
                hash_size[size] -= 1
                hash_size[new_size] = 1 + hash_size.get(new_size, 0)
            elif num - 1 in hash_chunks:
                (start, end, size) = hash_chunks[num - 1]
                start = start
                new_end = num
                new_size = size + 1
                hash_chunks[start] = (start, new_end, new_size)
                hash_chunks[num] = (start, new_end, new_size)
                hash_size[size] -= 1
                hash_size[new_size] = 1 + hash_size.get(new_size, 0)
            else:
                hash_chunks[num] = (num, num, 1)
                hash_size[1] = 1 + hash_size.get(1, 0)
            if m in hash_size and hash_size[m] > 0:
                last_found = i + 1
        return last_found
