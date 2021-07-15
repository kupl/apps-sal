S = set(list(input()))
cf = [chr(ord("a")+i) for i in range(26)]

for i in range(len(cf)):
    if cf[i] not in S:
        print(cf[i])
        return
print("None")
