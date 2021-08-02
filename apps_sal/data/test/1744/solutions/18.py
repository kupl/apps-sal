arr = list(map(int, input().split()))
n, m = arr[0], arr[1]
s = str(input())
a = [int(i) for i in s.split()]
answers = []
s = 0
count = 0
max_val = 0
k = 0
arr = [0 for i in range(101)]
for elem in a:
    if s + elem > m:
        i = max_val
        s2 = s
        c2 = count
        while s2 + elem > m:
            if s2 - arr[i] * i + elem <= m:
                ans = k - c2 + (arr[i] - (m - elem - (s2 - arr[i] * i)) // i)
                s2 -= i * (arr[i] - (m - elem - (s2 - arr[i] * i)) // i)
            else:
                s2 -= arr[i] * i
                c2 -= arr[i]
                i -= 1
        if elem < max_val:
            arr[elem] += 1
            arr[max_val] -= 1
            s = s - max_val + elem
            j = max_val
            while arr[j] < 1:
                j -= 1
            max_val = j
    else:
        arr[elem] += 1
        s += elem
        ans = k - count
        count += 1
        if elem > max_val:
            max_val = elem
    answers.append(str(ans))
    k += 1

print(' '.join(answers))
