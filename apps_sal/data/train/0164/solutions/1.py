class Solution:

    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k <= 0:
            return num
        if k > n * (n - 1) // 2:
            return ''.join(sorted(list(num)))
        for i in range(10):
            idx = num.find(str(i))
            if idx >= 0 and idx <= k:
                return num[idx] + self.minInteger(num[:idx] + num[idx + 1:], k - idx)
        'from collections import deque\n        j=0\n        \n        arr=[deque() for i in range(10)]\n        \n        n=len(num)\n        \n        for i in range(n):\n            arr[int(num[i])].append(i)\n            #print(arr)\n        \n        curr=0\n        ans=""\n        \n        def fun(x,y):\n            l=list(arr[x])\n            l.append(y)\n            l.sort()\n            arr[x]=deque(l)\n        \n        while k>0 and curr<n:\n            ch=None\n            ch_ind=curr\n            for i in range(0,int(num[curr])):\n                if arr[i] and arr[i][0]<=k:\n                    ch=i\n                    ch_ind=arr[i][0]\n                    arr[i].popleft()\n                    break\n                    \n            print(arr,ch,ch_ind,curr,k)\n            if ch:\n                ans+=str(ch)\n                k-=(ch_ind-curr)\n                \n            else:\n                ans+=num[curr]\n                curr+=1\n            print(ans)\n            \n        \n        return ans'
