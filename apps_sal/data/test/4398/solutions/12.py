N = int(input())
(S, T) = list(map(str, input().split()))
new_string = []
i = 0
for i in range(N):
    string1 = list(S).pop(i)
    string2 = list(T).pop(i)
    new_string.append(string1)
    new_string.append(string2)
    i += 1
new_string = ''.join(new_string)
print(new_string)
