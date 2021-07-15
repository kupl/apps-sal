def main():
	N = int(input())
	info = []
	for i in range(N):
		x, y, h = [int(a) for a in input().split(" ")]
		info.append({"x": x, "y": y, "h": h})
	info.sort(key=lambda f: -f["h"])
	for cx in range(101):
		for cy in range(101):
			H = 0
			for i in range(len(info)):
				h = info[i]["h"] + abs(info[i]["x"] - cx) + abs(info[i]["y"] - cy)
				if i == 0:
					H = h
				else:
					if h != H:
						if (info[i]["h"] == 0 and h < H) or (info[i]["h"] > 0):
							break
			else:
				print(cx, cy, H)
				return 0
	if info[0]["x"] in [0, 100] and info[0]["y"] in [0, 100]:
		print(info[0]["x"], info[0]["y"], info[0]["h"])
		return 0

main()
