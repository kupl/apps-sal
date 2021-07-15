names = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6,}

a = names[input().strip()]
b = names[input().strip()]

if (a == b) or ((a + 2) % 7 == b) or ((a + 3) % 7 == b):
	print("YES")
else:
	print("NO")


