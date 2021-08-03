m = int(input())
for h in range(m):
    n, b = list(map(int, input().split()))
    a = input()
    t = 0
    ans = []
    while b != 1:
        if a[t] == ')':
            for i in range(t, n):
                if a[i] == '(':
                    k = i
                    break
            c = a[t:k + 1]
            a = a[:t] + c[::-1] + a[k + 1:]
            #print(t, k, a)
            ans.append([t, k])
        if a[t + 1] == '(':
            for i in range(t + 1, n):
                if a[i] == ')':
                    k = i
                    break
            c = a[t + 1:k + 1]
            a = a[:t + 1] + c[::-1] + a[k + 1:]
            #print(t, k, a)
            ans.append([t + 1, k])
        t += 2
        b -= 1
    for i in range(t, t + (n - t) // 2):
        if a[i] == ')':
            for j in range(i, n):
                if a[j] == '(':
                    k = j
                    break
            #print(i, k)
            c = a[i:k + 1]
            a = a[:i] + c[::-1] + a[k + 1:]
            ans.append([i, k])
    # print(a)
    for i in range(t + (n - t) // 2, n):
        if a[i] == '(':
            for j in range(i, n):
                if a[j] == ')':
                    k = j
                    break
            c = a[i:k + 1]
            a = a[:i] + c[::-1] + a[k + 1:]
            ans.append([i, k])

    print(len(ans))
    for i in ans:
        print(i[0] + 1, i[1] + 1)
