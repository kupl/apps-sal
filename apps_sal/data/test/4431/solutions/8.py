(n, k) = list(map(int, input().strip().split()))
string = input().strip()
forbidden = input().strip().split()
forbidden = set(forbidden)
string = list(string)
for i in range(len(string)):
    if string[i] not in forbidden:
        string[i] = None
cnt = 0
i = 0
while i < len(string):
    if string[i] == None:
        i += 1
    else:
        j = i
        while j < len(string) and string[j] != None:
            j += 1
        diff = j - i
        cnt += diff * (diff + 1) // 2
        i = j
print(cnt)
