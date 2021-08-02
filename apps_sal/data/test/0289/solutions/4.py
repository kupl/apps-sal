'''input
KKKKKKV
'''
s = input().replace("VK", ".")
if "VV" in s or "KK" in s:
    print(s.count(".") + 1)
else:
    print(s.count("."))
