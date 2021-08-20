from sys import stdin as Si
from collections import defaultdict as dt
from operator import itemgetter as ig


def __starting_point():
    (n, m) = list(map(int, Si.readline().split()))
    h = dt(dict)
    for i in range(n):
        (s, r, p) = list(map(str, Si.readline().split()))
        (r, p) = list(map(int, (r, p)))
        if p in h[r]:
            h[r][p] += [s]
        else:
            h[r][p] = [s]
    for da in h:
        d = sorted(list(h[da].items()), key=ig(0), reverse=True)
        (ns, i) = ([], 0)
        while len(ns) < 2:
            if len(d[i][1]) + len(ns) >= 3:
                ns = '?'
                break
            else:
                ns += d[i][1][:2 - len(ns)]
            i += 1
            if i >= len(d):
                break
        print(' '.join(ns))


'\nVery soon Berland will hold a School Team Programming Olympiad. From each of the m Berland regions a team of two people is invited to participate in the olympiad. The qualifying contest to form teams was held and it was attended by n Berland students. There were at least two schoolboys participating from each of the m regions of Berland. The result of each of the participants of the qualifying competition is an integer score from 0 to 800 inclusive.\n\nThe team of each region is formed from two such members of the qualifying competition of the region, that none of them can be replaced by a schoolboy of the same region, not included in the team and who received a greater number of points. There may be a situation where a team of some region can not be formed uniquely, that is, there is more than one school team that meets the properties described above. In this case, the region needs to undertake an additional contest. The two teams in the region are considered to be different if there is at least one schoolboy who is included in one team and is not included in the other team. It is guaranteed that for each region at least two its representatives participated in the qualifying contest.\n\nYour task is, given the results of the qualifying competition, to identify the team from each region, or to announce that in this region its formation requires additional contests.\nInput\n\nThe first line of the input contains two integers n and m (2\u2009≤\u2009n\u2009≤\u2009100\u2009000, 1\u2009≤\u2009m\u2009≤\u200910\u2009000, n\u2009≥\u20092m) — the number of participants of the qualifying contest and the number of regions in Berland.\n\nNext n lines contain the description of the participants of the qualifying contest in the following format: Surname (a string of length from 1 to 10 characters and consisting of large and small English letters), region number (integer from 1 to m) and the number of points scored by the participant (integer from 0 to 800, inclusive).\n\nIt is guaranteed that all surnames of all the participants are distinct and at least two people participated from each of the m regions. The surnames that only differ in letter cases, should be considered distinct.\nOutput\n\nPrint m lines. On the i-th line print the team of the i-th region — the surnames of the two team members in an arbitrary order, or a single character "?" (without the quotes) if you need to spend further qualifying contests in the region.\nExamples\nInput\n\n5 2\nIvanov 1 763\nAndreev 2 800\nPetrov 1 595\nSidorov 1 790\nSemenov 2 503\n\nOutput\n\nSidorov Ivanov\nAndreev Semenov\n\nInput\n\n5 2\nIvanov 1 800\nAndreev 2 763\nPetrov 1 800\nSidorov 1 800\nSemenov 2 503\n\nOutput\n\n?\nAndreev Semenov\n\nNote\n\nIn the first sample region teams are uniquely determined.\n\nIn the second sample the team from region 2 is uniquely determined and the team from region 1 can have three teams: "Petrov"-"Sidorov", "Ivanov"-"Sidorov", "Ivanov" -"Petrov", so it is impossible to determine a team uniquely.\n'
__starting_point()
