a = list(map(int, list(input())))

if a[0] % 3 == 0:
    cnt = 1
    last_free = 1
else:
    cnt = 0
    last_free = 0

for i in range(1, len(a)):
    if (a[i] % 3 == 0):
        cnt += 1
        last_free = i + 1
    else:
        sm = 0
        # print(i)
        for j in range(i, last_free - 1, -1):
            sm += a[j]
            # print(j, end=", ")
            if sm % 3 == 0:
                #print("GOT")
                cnt += 1
                last_free = i + 1
                break
        #print("")
print(cnt)

