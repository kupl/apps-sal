n = int(input())
s = list(map(set, input().split()))
final = []
for i in s:
    for j in final:
        if i == j:
            break
    else:
        final.append(i)
print(len(final))

