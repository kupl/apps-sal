

no_of_sold = int(input())
weapons = input()

weapons = weapons.split(' ')
counter = 0
for wea in weapons:
	if (int(wea)%2 == 0):
		counter += 1
	else:
		counter -= 1

if(counter > 0):
	print("READY FOR BATTLE")
else:
	print("NOT READY")
