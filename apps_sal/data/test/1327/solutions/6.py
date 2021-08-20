(N, M) = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
cand = []
wxyz = [tmp[0] + tmp[1] + tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [tmp[0] + tmp[1] - tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [tmp[0] - tmp[1] + tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [tmp[0] - tmp[1] - tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [-tmp[0] + tmp[1] + tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [-tmp[0] + tmp[1] - tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [-tmp[0] - tmp[1] + tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
wxyz = [-tmp[0] - tmp[1] - tmp[2] for tmp in xyz]
wxyz.sort(reverse=True)
cand.append(sum(wxyz[:M]))
print(max(cand))
