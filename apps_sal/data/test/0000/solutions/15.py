import sys
s = input()
l = len(s)
s_list = [x for x in s]

counter = 0
try:
	a = s_list.index('[')
	counter += a
	s_list = s_list[a + 1:]
except:
	print(-1)
	return

try:
	a = s_list.index(':')
	counter += a
	s_list = s_list[a + 1:]
except:
	print(-1)
	return

s_list_rev = s_list.copy()
s_list_rev.reverse()

try:
	b = s_list_rev.index(']')
	counter += b
	s_list_rev = s_list_rev[b+1:]
except:
	print(-1)
	return

try:
	b = s_list_rev.index(':')
	counter += b
	s_list_rev = s_list_rev[b+1:]
except:
	print(-1)
	return
s_list_rev = [x for x in s_list_rev if x != '|']
counter += len(s_list_rev)
print(l - counter)
