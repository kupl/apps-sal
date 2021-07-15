k = int(input())
count = {i:0 for i in "123456789."}

for i in range(4):
    for string in input():
        count[string] += 1;

count["."] = 0

if max(count.values()) > 2*k:
    print("NO")
else:
    print("YES")

