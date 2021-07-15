N = int(input())
materials = list(map(int, input().split()))

for _ in range(N-1):
	materials.sort()
	new_material = (materials[0] + materials[1])/2
	materials.pop(0)
	materials.pop(0)
	materials.append(new_material)
	
print(materials[0])
