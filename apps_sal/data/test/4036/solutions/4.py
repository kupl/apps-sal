

n, k = list(map(int, input().split()))

d = [0]*k

if k == 1:
    print ('YES')
    print (n)
else:
    for i in range(k):
        d[i] = i + 1

    if sum(d) > n:
        print ('NO')
    else:
        t = n - sum(d)

        if t >= k:

            a = t // k
            t = t % k
            for i in range(k):
                d[i] += a

        if t > 0:
            if d[0] > 1:

                for i in range(k-1, k-1-t, -1):
                    d[i] += 1

            elif d[0] == 1:

                for i in range(k-1, 1, -1):
                    d[i] += 1
                    t -= 1
                    if t == 0: 
                        break


                if t > 0:
                    for i in range(k-1, 2, -1):
                        d[i] += 1
                        t -= 1
                        if t == 0: 
                            break


        # print (d)
        chk = True
        for i in range(k - 1):
            if d[i + 1] > 2 * d[i]:
                chk = False
                break

        if sum(d) != n:
            chk = False
            
        if chk:    
            print ('YES')
            s = ""
            for i in d:
                s += str(i) + " "
            print(s[:-1])
        else:
            print ('NO')


