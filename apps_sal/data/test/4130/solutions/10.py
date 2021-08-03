n = int(input())
ms = sorted(map(int, input().split()))
ws = set()
for i in ms:
    if (i != 1 and i - 1 not in ws):
        ws.add(i - 1)
    elif (i not in ws):
        ws.add(i)
    elif (i + 1 not in ws):
        ws.add(i + 1)
print(len(ws))
