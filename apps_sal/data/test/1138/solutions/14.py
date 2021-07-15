s = input()

ans = -1

if len(s) % 2 == 0:
	UD = abs(s.count("U")-s.count("D"))
	LR = abs(s.count("L")-s.count("R"))
	
	ans = (UD+LR)//2

print(ans)
