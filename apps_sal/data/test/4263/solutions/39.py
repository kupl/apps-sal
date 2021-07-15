s = input() + 'I'
List = []

for i in range(len(s)):
    count = 0
    for j in range(len(s) - i):
        if s[i] == 'A' or s[i] == 'T' or s[i] == 'G' or s[i] == 'C':
            count += 1
            i += 1
        else:
            List.append(count)
            break

print(max(List))
