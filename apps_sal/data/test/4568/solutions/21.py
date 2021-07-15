n = int(input())
s = input()

count = []
for i in range(1,n):
    first = s[:i]
    second= s[i:]
    # print(first,second)
    count.append(len(set(first)&set(second)))

# print(count)
print((max(count)))

