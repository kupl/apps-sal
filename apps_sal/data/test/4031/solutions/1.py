from functools import cmp_to_key
def mycmp(a, b):
    if a == b:
        return 0
    if a in b:
        return -1
    return 1

def main():
    n = int(input())
    a = [input() for _ in range(n)]
    poss = True
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] not in a[j] and a[j] not in a[i]:
                poss = False
    if not poss:
        print('NO')
        return
    a.sort(key=cmp_to_key(mycmp))
    print('YES')
    for x in a:
        print(x)
main()

