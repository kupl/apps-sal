DEBUG = False
n, v = [int(x) for x in input().split()]
fruits = []
for i in range(n):
    aa, bb = [int(x) for x in input().split()]
    fruits.append([aa, bb])

fruits.sort()

day, t_harvested, tot, curr = 0, 0, 0, []


def remove_old():
    while fruits != [] and fruits[0][0] < day - 1:
        t = fruits.pop(0)
        if DEBUG: print("Rotten {} on day {}".format(t, day))
    while curr != [] and curr[0][0] < day - 1:
        curr.pop(0)
        #print("Rotten/harvested {} on day {}".format(t, day))


def add_current():
    for f in fruits:
        if day - 1 <= f[0] <= day:
            curr.append(f)
            if DEBUG: print("New fruit {} on day {}".format(f, day))


def harvest_todays():
    nonlocal t_harvested
    nonlocal tot

    while curr != []:
        t = curr.pop(0)
        harvest = min(t[1], v - t_harvested)
        if DEBUG: print("Harvested {} of {} on day {}".format(harvest, t, day))
        t_harvested += harvest
        t[1] -= harvest
        tot += harvest
        # if harvest == 0: ## BUG!!!
        #	break


while fruits != []:

    remove_old()

    add_current()

    harvest_todays()
    day += 1
    t_harvested = 0

print(tot)
