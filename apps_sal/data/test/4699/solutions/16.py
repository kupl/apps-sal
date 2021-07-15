n, k = input().split()
d = list(map(int, input().split()))

a = []

for i in range(10):
    if i not in d:
        a.append(i)

n = list(map(int, list(n)))

for i in range(len(n)):
    if n[i] in d:
        ind = i

        done = False
        while not done:
            for j in range(n[ind]+1, 10):
                if j in a:
                    n[ind] = j
                    done = True
                    break

            if not done:
                ind -= 1

                if ind < 0:
                    n.insert(0, a[1] if a[0] == 0 else a[0])
                    ind = 0
                    done = True

        for j in range(ind+1, len(n)):
            n[j] = a[0]

        break

print("".join(list(map(str, n))))
