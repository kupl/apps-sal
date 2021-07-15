import sys

s = input()
s_reverse = s[::-1]
t = input()

first = []
second = []

pos = 0

def find_str(st, char):
    index = 0
    if char in st:
        # print("===")
        c = char[0]
        for ch in st:
            if ch == c:
                if st[index:index+len(char)] == char:
                    return index
            index += 1
            # print (index)
    return -1

while pos < len(t):
	substr = t[pos:pos + 1]
	if substr not in s and substr not in s_reverse:
		print("-1")
		return
	step = 1
	while substr in s or substr in s_reverse:
		step += 1
		substr = t[pos:(pos + step)]
		# print("substr %s" % substr)
		if pos + step > len(t):
			break
	step -= 1
	substr = t[pos:(pos + step)]
	start = find_str(s, substr)
	# print ("debug %d %d %d" % (pos, step, start))
	if start == -1:
		start = find_str(s_reverse, substr)
		# print ("newstart: %d" % start)
		# print("substr %s" % substr)	
		first.append(len(s) - start)
		second.append(len(s) - (start + step - 1))
	else:
		first.append(start + 1)
		second.append(start + step)
	pos = pos + step
	# print ("last %d %d" %(len(t), pos))

print(len(first))
for a, b in zip(first, second):
	print("%d %d" % (a, b))

# x = input("ccc")


