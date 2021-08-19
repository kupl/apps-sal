import sys
(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
left = 1
right = n + 1
ans = 10 ** 18 + 1
while left != right:
    mid = (left + right) // 2
    din = 0
    kaam = 0
    c = 0
    for i in l:
        if i - din <= 0:
            break
        kaam += i - din
        c += 1
        if c == mid:
            c = 0
            din += 1
    if kaam >= m:
        ans = min(ans, mid)
        right = mid
    else:
        left = mid + 1
if ans == 10 ** 18 + 1:
    print(-1)
else:
    print(ans)
'\nimport sys\nn = int(input())\nl = list(map(int,input().split()))\n\nfreq = [0]*1001\n\nfor i in range(n*n):\n    freq[l[i]] += 1\n\nodd = oc = 0\ntwo = []\nprint(freq[:11])\nif n > 2:\n    mn = 4\n    \n    for i in range(1001):\n        if freq[i] != 0:\n            \n            if freq[i]%2 == 1:\n                odd = i\n                oc += 1\n                freq[i] -= 1\n            if freq[i]%2 == 0 and freq[i]%4 != 0:\n                two.append(i)\n                freq[i] -= freq[i]%4\n                continue\n                \n            if freq[i]%4 != 0:\n                print(\'NO\')\n                return\n                \nans = [ [0]*n for i in range(n) ]\n\nif not n%2 and odd != 0:\n    print(\'NO\')\n    return\n\n\nif oc > 1:\n    print(\'NO\')\n    return\n    \nif n%2:\n    ans[n//2][n//2] = odd\n\nr = c = 0\n\nprint(two)\nprint(freq[:11])\nmid = 0\nfor i in range(n):\n    for j in range(n):\n        if ans[i][j] == 0:\n            for k in range(1,1001):\n                if freq[k] != 0:\n                    temp = k\n                    r = i\n                    c = j\n\n                    ans[r][c] = ans[n-1-r][c] = ans[r][n-1-c] = ans[n-1-r][n-1-c] = temp\n                    flag = False\n                    if n%2 and ( n//2 == i or n//2 == j):\n                        #print(\'are ye to odd hai\')\n                        if len(two) != 0:\n                            ans[n//2][mid] = ans[n//2][n-mid-1] = two[-1]\n                            flag = True\n                            two.pop()\n                        else:\n                            ans[n//2][mid] = ans[n//2][n-mid-1] = temp\n                        mid+=1\n                    #print(freq[:7])\n                    if not flag:\n                        freq[k] =freq[k] - 4\n                    else:\n                        freq[k] = freq[k] - 2\n                    #print(freq[:7])\n                    break\nprint("YES")\nfor i in range(n):\n    print(*ans[i])\n'
