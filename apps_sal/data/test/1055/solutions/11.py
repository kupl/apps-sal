n = int(input())
l = list(map(int, input().split()))

def isSorted(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def sort(a):
    if isSorted(a):
        return a
    t = len(a) // 2
    a1 = a[:t]
    a2 = a[t:]
    a1 = sort(a1)
    a2 = sort(a2)
    if (len(a1) >= len(a2)):
        return a1
    else:
        return a2

print(len(sort(l)))

