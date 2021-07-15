#ABC141B
s = input()
print("Yes" if (s[::2].count("L")+s[1::2].count("R"))==0 else "No")
