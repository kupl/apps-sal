n, p, k = list(map(int, input().split()))

output = []
start = max(1, p - k)
end = min(n, p + k)
if start != 1:
    output.append("<<")
for i in range(start, end + 1):
    if i == p:
        output.append("(" + str(i) + ")")
    else:
        output.append(str(i))
if end != n:
    output.append(">>")

print(" ".join(output))
