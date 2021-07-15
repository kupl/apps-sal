N = int(input())
a = map(int, input().split())
counter = 0
for ai in a:
    if counter + 1 == ai:
        counter += 1
print(N - counter if counter != 0 else '-1')
