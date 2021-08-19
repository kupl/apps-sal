class Solution:

    def minOperations(self, n: int) -> int:
        sum_tot = 0
        for i in range(n):
            val = 2 * i + 1
            if val > n:
                sum_tot += val - n
            else:
                sum_tot += n - val
        return int(sum_tot / 2)
        '\n        if n%2  == 0:\n            median = int((arr[int(n/2)] + arr[int(n/2)-1])/2)\n        else:\n            median = arr[int(n/2)]\n        print(median)\n        \n        ctr = 0\n        while(len(set(arr)) > 1):\n            min_elem = arr[-1] + 1\n            max_elem = -1\n            min_ind = -1\n            max_ind = -1\n            for i in range(len(arr)):\n                if arr[i] > max_elem:\n                    max_elem = arr[i]\n                    max_ind = i\n                if arr[i] < min_elem:\n                    min_elem = arr[i]\n                    min_ind = i\n            arr[max_ind] -= 1\n            arr[min_ind] += 1\n            ctr += 1\n        \n        return ctr\n        '
