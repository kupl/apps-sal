from collections import Counter
moji = str(input())
guall = len(moji) // 2
kiall = guall + len(moji) % 2
gucount = dict(Counter(moji[1::2]))
kicount = dict(Counter(moji[0::2]))
if len(moji) == 1:
    ans = 0
elif max(gucount, key=gucount.get) != max(kicount, key=kicount.get):
    ans = guall - max(gucount.values()) + kiall - max(kicount.values())
elif kiall - max(kicount.values()) > guall - max(gucount.values()):
    ans = max(kicount.values()) + guall - max(gucount.values())
else:
    ans = max(gucount.values()) + kiall - max(kicount.values())
print(ans)
