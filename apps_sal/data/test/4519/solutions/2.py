for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    zeroes = []
    for i in range(n):
        if s[i] == '0':
            zeroes.append(i)
    s = list(s)
    ind = 0
    le = len(zeroes)
    i = 0
   # print(zeroes)
    while i < n:
      #  print(k)
        if s[i] == '1':
            while ind < le and zeroes[ind] < i:
                ind += 1
            if ind == le:
                break
            a = zeroes[ind]
            # print(a)
           # print(i,a)
            if a - i <= k:
                k -= (a - i)
                s[i], s[a] = s[a], s[i]
                # print(s)
                ind += 1
            # ind+=1
        i += 1
    print(''.join(s))
