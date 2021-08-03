# python3
# utf-8

visits_nr = int(input())
ro_dist = int(input())
rd_dist = int(input())
od_dist = int(input())
# pref_end_r___min_dist
# pref_end_o___min_dist
# pref_end_d___min_dist
pref_end_r___min_dist = [0] * visits_nr
pref_end_o___min_dist = [10**9] * visits_nr
pref_end_d___min_dist = [10**9] * visits_nr
for visit in range(1, visits_nr):
    pref_end_r___min_dist[visit] = min(pref_end_o___min_dist[visit - 1] + ro_dist, pref_end_d___min_dist[visit - 1] + rd_dist)
    pref_end_o___min_dist[visit] = min(pref_end_r___min_dist[visit - 1] + ro_dist, pref_end_d___min_dist[visit - 1] + od_dist)
    pref_end_d___min_dist[visit] = min(pref_end_o___min_dist[visit - 1] + od_dist, pref_end_r___min_dist[visit - 1] + rd_dist)
ans = min((pref_end_d___min_dist[-1], pref_end_o___min_dist[-1], pref_end_r___min_dist[-1]))
print(ans)
