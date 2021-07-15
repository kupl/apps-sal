a, b, c = list(map(int, input().split()))
data = [a]
if not b in data:
    data.append(b)
if not c in data:
    data.append(c)
print(len(data))
