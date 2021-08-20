n = int(input())
array = list(map(int, input().strip().split()))
dodani = set()
new = []
for e in array[::-1]:
    if e not in dodani:
        dodani.add(e)
        new.append(e)
print(len(new))
print(' '.join(list(map(str, new[::-1]))))
