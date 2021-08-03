def divide(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = int(l[i] / 2)
        else:
            return False

    return True


n = int(input())
l = list(map(int, input().split()))

count = 0
while divide(l):
    count += 1

print(count)
