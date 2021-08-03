class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        def find_n_sum(arr, target, N, l, r, path, output):
            if arr[l] * N > target or arr[r] * N < target:
                return

            if N == 2:
                s, e = l, r
                while s < e:
                    total = arr[s] + arr[e]
                    if total < target or s > l and arr[s - 1] == arr[s]:
                        s += 1
                    elif total > target or e < r and arr[e] == arr[e + 1]:
                        e -= 1
                    else:
                        output.add(tuple(path + [arr[s], arr[e]]))
                        s += 1
                        e -= 1
            else:
                for i in range(l, r + 1 - (N - 1)):
                    if i > l and arr[l] == arr[l - 1]:
                        continue

                    find_n_sum(arr, target - arr[i], N - 1, i, r, path + [arr[i]], output)

        combos = set()
        res = 0
        counter = Counter(A)
        new_arr = []
        for k in sorted(counter.keys()):
            new_arr += [k] * min(counter[k], 3)

        find_n_sum(new_arr, target, 3, 0, len(new_arr) - 1, [], combos)

        for lst in combos:
            cnt = 1
            temp = Counter(lst)
            for k in temp:
                for i in range(temp[k]):
                    cnt *= (counter[k] - i) / (i + 1)

            res = (res + cnt) % (10**9 + 7)

        return int(res) % (10**9 + 7)
