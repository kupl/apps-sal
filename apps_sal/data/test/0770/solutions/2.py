input()
s="".join(input().split())
clicks = s.count("1") + len(s.replace("0", " ").split()) - 1
print(max(0, clicks))


