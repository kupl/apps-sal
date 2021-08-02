n, k = list(map(int, input().split()))
a = list(map(str, input().split()))


while True:

    for j in str(n):

        if j in a:
            break
    else:
        break
    n += 1

print(n)
