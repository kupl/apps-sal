(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [-1] * (n + 1)
tmp = []
here = 1
count = 0
while True:
    if b[here] != -1:
        roop = count - b[here]
        if k < count:
            print(tmp[k])
        else:
            new_tmp = tmp[b[here]:]
            s = k - b[here]
            print(new_tmp[s % roop])
        break
    b[here] = count
    count += 1
    tmp.append(here)
    here = a[here - 1]
