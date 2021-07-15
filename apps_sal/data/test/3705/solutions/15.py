N = int(input())

ipt = input()

def checker(ipt):
    if "8" in ipt:
        if len(ipt) >= 11:
            return min(len(ipt)//11, ipt.count("8"))
    return 0

print(checker(ipt))
