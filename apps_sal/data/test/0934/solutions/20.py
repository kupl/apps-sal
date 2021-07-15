import sys
import math

def read_int():
	return int(input().strip())

def read_int_list():
	return list(map(int,input().strip().split()))

def read_string():
	return input().strip()

def read_string_list(delim=" "):
	return input().strip().split(delim)

###### Author : Samir Vyas #######
###### Write Code Below    #######

table_c = read_string()

cards = read_string_list()

for c in cards:
	if c[0] == table_c[0] or c[1] == table_c[1]:
		print("YES")
		return

print("NO")
