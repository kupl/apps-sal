import sys, math, itertools

n = int(input())
towns = [[int(x) for x in row.split()] for row in sys.stdin.readlines()]

counter = 0
final_sum = 0
for town_list in itertools.permutations(towns):
#    print("town_list",town_list)
    counter += 1
    sum = 0
    for i,town in enumerate(town_list):
#        print("town",town)
        if i == 0:
            old_town = town
        else:
            length = math.sqrt((town[0]-old_town[0])**2 + (town[1]-old_town[1])**2)
#            print("length",length)
            sum += length
#            print("sum",sum)
            old_town = town
    final_sum += sum
print(final_sum/counter)
