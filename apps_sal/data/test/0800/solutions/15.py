from math import atan2, degrees, pi

def main():
	num_man = int(input())
	angles = []
	for n in range(num_man):
		x, y = input().strip().split(' ')
		x, y = int(x), int(y)
		angles.append(atan2(y, x))
	angles.sort()
	max_diff = 0
	for i in range(len(angles) - 1):
		max_diff = max(max_diff, angles[i + 1] - angles[i])
	diff = angles[0] - angles[num_man - 1]
	if diff < 1e-7:
		diff += 360 * pi / 180
	max_diff = max(max_diff, diff)
	res = 360 - (max_diff * 180 / pi)
	print(res)

main()
