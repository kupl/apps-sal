w, m, k = map(int, input().split())
L = len(str(m))
end = m
flag = False
while True:
    if w > (10 ** L - end) * k * L:
        w -= (10 ** L - end) * k * L
        end = 10 ** L
        L += 1
        #if w < L * k:
            #print(end - m)
            #flag = True
            #break
        #else:
            #w -= L * k
            #end = 10 ** L + 1
    else:
        end += w // (L * k)
        break

if not(flag):
    print(end - m)
