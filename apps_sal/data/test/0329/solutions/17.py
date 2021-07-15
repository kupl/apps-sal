import math;

s = input();
size = len(s);
letters = [0, 0, 0, 0]
n = 0;
i = 0;
e = 0;
t = 0;

for x in range(0, size):
	if s[x] == "n":
		n += 1;
	elif s[x] == "i":
		i += 1;
	elif s[x] == "e":
		e += 1;
	elif s[x] == "t":
		t += 1;
		
if (n == 3):
  n = 1;
elif (n < 3):
  n = 0;
else:
  n -= 3;
  n = math.floor(n / 2);
  n += 1;

e = math.floor(e / 3);

letters[0] = n;
letters[1] = i;
letters[2] = e;
letters[3] = t;

print((min(letters)));
# 1502216507489

