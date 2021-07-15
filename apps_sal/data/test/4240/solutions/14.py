S = input()
T = input()

def rolling(str , n):
    return str[n:len(str)] + str[:n]

for i in range(len(S)):
    if T == rolling(S, i):
        print('Yes')
        return

print('No')
