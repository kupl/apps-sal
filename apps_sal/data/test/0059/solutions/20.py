n = int(input())
s = input().split()
arr = []
for l in s:
    arr.append(int(l))
s = input()
k = len(s)
pos = []
for l in s:
    pos.append(int(l))

i = 0
indexset = set()
valueset = set()
while i < k:
    if pos[i] == 0:
        if arr[i] != i + 1:
            print("NO")
            return

    if pos[i] == 1:
        while i < k:
            if pos[i] == 1:
                indexset.add(i+1)
                valueset.add(arr[i])
                i += 1
            else:
                break
        indexset.add(i+1)
        valueset.add(arr[i])
        if len(indexset ^ valueset) > 0:
            print("NO")
            return
        indexset.clear()
        valueset.clear()

    i += 1
print("YES")
