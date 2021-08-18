n = int(input())
s = input()

exi = [0 for i in range(52)]


def fill(x):
    if(x.islower()):
        exi[ord(x) - 97] = 1
        return ord(x) - 97
    else:
        exi[ord(x) - 65 + 26] = 1
        return ord(x) - 65 + 26


arr = []
for c in s:
    arr.append(fill(c))

now = [0 for i in range(52)]


def check():
    for i in range(52):
        if(exi[i]):
            if(exi[i] > now[i]):
                return 0
    return 1


first = 0
now[arr[first]] += 1
if(check()):
    print(1)
    return

min = n
for i in range(1, n):
    now[arr[i]] += 1
    for j in range(first, i):
        if(now[arr[j]] > 1):
            first += 1
            now[arr[j]] -= 1
        else:
            break
    if(check()):
        leng = i - first + 1
        if(min > leng):
            min = leng
print(min)
